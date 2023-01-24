import threading

def super_monkey_face():
  print("🐵来い" * 500)

def main():
  threading.Thread(target=super_monkey_face).start()

if __name__ == "__main__":
  main()
