import pyautogui, time

msg = "Salom!"
n = 1000

print(" Boshlandi! ")

count = 5

while(count !=5):
	time.sleep(1)
	count -= 1
print("\n Tugadi!")

for i in range(0, int(n)):
	pyautogui.typewrite(msg + '\n')
