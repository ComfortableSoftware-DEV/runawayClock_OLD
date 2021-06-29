

def one(
	*args_,
	**KWArgs_,
):
	print(f"""args_ {args_}
KWArgs_ {KWArgs_}
""")
	if (
			(args_ != ())
	):
		print(f"""args_[0] {args_[0]}""")

one(
		("__SUB0__", "_00"),
		("__SUB1__", "CF"),
		("__SUB2__", "APPDS"),
)
