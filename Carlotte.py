def main():

	print("比較したい長さを入力するであります。(cm)")

	try:
		yourSize = float(input('>>'))#inputSize
		CHARLOTTE = 90.
		PUNIANA = 22  #Puniana_size


		q = round((yourSize / CHARLOTTE), 3)
		y = round((yourSize / PUNIANA), 3)

		if 	yourSize == 90:
			print("これは私と同じ大きさでありますね!")

		elif yourSize == 22:
			print("それぷにあなと同じサイズじゃんｗｗｗｗｗｗ")

		elif yourSize == 114514 or yourSize == 810 or yourSize == 114 or yourSize == 514:
			print("うっわｗ淫夢厨じゃんｗｗｗこれだからホモガキはなぁ.......。")

		else:
			print(" {} cmは".format(str(yourSize))+str(q)+"シャルロッテであります。")
			print(" {} cmは".format(str(yourSize))+str(y)+"ぷにあなであります。")


	except:
		print("Error")
		exit()


if __name__ == '__main__':
	main()



