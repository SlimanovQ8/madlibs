def main():
	# write your code here
	print("Mad libs where libs get mad. \n Start below: ")
	time = input("Enter a number from 1 to 12: ")
	items = input("Enter  a noun  (plural): ")
	name = input("Enter a name: ")
	scream = input("Enter any sentence: ")
	verb = input("Enter a verb: ")
	print(f"It was, {time} o'clock when I heard knock a door. ")
	print(f"I opened the door and there was a box full of, {items} with a note saying \"From Mr. {name.title()}\".")
	print(f"Just as I closed the door I heard a scream \"{scream.upper()}\".")
	print(f"I froze in place and all I {verb}.")
	

if __name__ == '__main__':
	main()