prefix = "oo3/"

def sampleSplit(file_name):
    sample_file = open(prefix+file_name, "r")
    index = -1;
    info_file = None
    in_file = None
    out_file = None
    hand_file = open(prefix+"sample_hand.txt", "w")
    first_out_flag = False
    first_out_flag = False
    for line in sample_file.readlines():
        line = line.lstrip()
        if(len(line) == 0):
            hand_file.write("\n")
            continue

        sign = line[0]
        line = line[1:len(line)-1]#remove \n
        if(sign == '#'):
            if(info_file):
                info_file.close()
                in_file.close()
                out_file.close()

            index = index + 1
            info_file = open(prefix+str(index)+".info", "w")
            in_file = open(prefix+str(index)+".in", "w")
            out_file = open(prefix+str(index)+".out", "w")
            first_in_flag = True
            first_out_flag = True

            info_file.write(line)
            hand_file.write("#" + line + "\n")
        elif sign == '<':
            if(not first_in_flag):
                in_file.write("\n")
            first_in_flag = False
            in_file.write(line)
            hand_file.write(line+"\n")
        elif sign == '>':
            if(not first_out_flag):
                out_file.write("\n")
            first_out_flag = False
            line.replace(" ", "")
            out_file.write(line)
            hand_file.write(line+"\n")

    if(info_file):
        info_file.close()
        in_file.close()
        out_file.close()
    hand_file.close()
    sample_file.close()

sampleSplit("sample.txt")

		
	
