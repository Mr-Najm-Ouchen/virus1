import random
import time
import pyautogui

# مدة التشغيل العشوائي (60 ثانية)
duration = 60

# الوقت الحالي
start_time = time.time()

while time.time() - start_time < duration:
    # توليد أحداث عشوائية (تحريك الفأرة، ضغط مفاتيح)
    action = random.choice(['move', 'click', 'type'])

    if action == 'move':
        # تحريك الفأرة إلى موضع عشوائي
        x = random.randint(0, 1920)  # استبدل 1920 بعرض الشاشة
        y = random.randint(0, 1080)  # استبدل 1080 بارتفاع الشاشة
        pyautogui.moveTo(x, y, duration=0.5)

    elif action == 'click':
        # الضغط على زر الفأرة في موضع عشوائي
        pyautogui.click()

    elif action == 'type':
        # كتابة نص عشوائي
        text = random.choice(['Hello!', 'Python!', 'Random!'])
        pyautogui.typewrite(text, interval=0.2)

    # الانتظار لفترة قصيرة بين الأحداث
    time.sleep(random.uniform(0.5, 1.5))
