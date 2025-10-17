import datetime

def main():
  print("Hello, World!")

  # Get current time and print it
  current_time = datetime.datetime.now()

  print("Current time:", current_time)
  print("Test change on branch to check trigger of workflow upon pull request")

if __name__ == "__main__":
  main()
