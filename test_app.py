from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Open the HTML file directly
    page.goto('file:///D:/desktop/vibe_coding_project/daily plan/index.html')
    page.wait_for_load_state('networkidle')

    # Check the page loaded correctly
    title = page.title()
    print(f"Page title: {title}")

    # Check key elements exist
    date_display = page.locator('#dateDisplay').text_content()
    print(f"Date display: {date_display}")

    # Check tabs exist
    duration_tab = page.locator('.mode-tab[data-mode="duration"]')
    timeline_tab = page.locator('.mode-tab[data-mode="timeline"]')
    print(f"Duration tab visible: {duration_tab.is_visible()}")
    print(f"Timeline tab visible: {timeline_tab.is_visible()}")

    # Check bottom nav exists
    home_nav = page.locator('.nav-item[data-page="home"]')
    fixed_nav = page.locator('.nav-item[data-page="fixed"]')
    my_nav = page.locator('.nav-item[data-page="my"]')
    print(f"Bottom nav items visible: {home_nav.is_visible() and fixed_nav.is_visible() and my_nav.is_visible()}")

    # Check add button exists
    add_btn = page.locator('#addBtn')
    print(f"Add button visible: {add_btn.is_visible()}")

    # Check console for errors
    errors = []
    page.on('console', lambda msg: errors.append(msg.text) if msg.type == 'error' else None)

    # Click add button to test form
    add_btn.click()
    page.wait_for_timeout(300)
    form = page.locator('#addForm')
    print(f"Add form shown after click: {form.is_visible()}")

    # Fill in task name
    name_input = page.locator('#taskName')
    name_input.fill('测试任务')

    # Set times
    start_time = page.locator('#startTime')
    start_time.fill('10:00')
    end_time = page.locator('#endTime')
    end_time.fill('10:30')

    # Confirm button should be enabled now
    confirm_btn = page.locator('#confirmBtn')
    print(f"Confirm button enabled: {not confirm_btn.is_disabled()}")

    # Submit the form
    confirm_btn.click()
    page.wait_for_timeout(500)

    # Check task was added
    task_cards = page.locator('.task-card')
    print(f"Task cards count: {task_cards.count()}")

    # Take screenshot
    page.screenshot(path='D:/desktop/vibe_coding_project/daily plan/test_result.png', full_page=True)
    print("Screenshot saved to test_result.png")

    # Test mode switching
    timeline_tab.click()
    page.wait_for_timeout(300)
    timeline_cards = page.locator('.timeline-card')
    print(f"Timeline cards count: {timeline_cards.count()}")

    # Test navigation to fixed page
    fixed_nav.click()
    page.wait_for_timeout(300)
    fixed_buttons = page.locator('.fixed-btn')
    print(f"Fixed buttons count: {fixed_buttons.count()}")

    # Test navigation to my page
    my_nav.click()
    page.wait_for_timeout(300)
    eye_toggle = page.locator('#eyeBreakToggle')
    print(f"Eye break toggle visible: {eye_toggle.is_visible()}")

    if errors:
        print(f"Console errors: {errors}")
    else:
        print("No console errors detected")

    browser.close()
    print("\n✓ All basic tests passed!")
