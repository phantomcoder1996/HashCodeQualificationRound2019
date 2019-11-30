import numpy as np
import argparse




class slide(object):
    def __init__(self,id,tags,type):
        self.tags = tags
        self.id = id
        self.type = type

    def convert_tags_to_int(self,tags):
        self.tags = [tags[t] for t in self.tags]

    def get_num_tags(self):
        return len(self.tags)


def convert_vertical_to_horizontal(v):
    pass



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--infile","-i")
    parser.add_argument("--outfile","-o")

    args = parser.parse_args()
    infile = args.infile
    outfile = args.outfile


    vs = []
    hs = []
    tags = {}
    tag_id = 1

    with open(infile,"r") as f:
        lines = [line[:-1] if line[-1]=="\n" else line for line in f.readlines()]
        n = int(lines[0])
        photos = lines[1:]
        for i,photo in enumerate(photos):
            x = photo.split(" ")
            ts = x[2:]
            if x[0]=="V":
                vs.append(slide(i,ts,"V"))

            else:
                hs.append(slide(i,ts,"H"))

            for t in ts:
                if tags.get(t)==None:
                    tags[t]=tag_id
                    tag_id+=1
        print("Num vertical = {}".format(len(vs)))
        print("Num horizontal = {}".format(len(hs)))

        for photo in vs:
            photo.convert_tags_to_int(tags)
        for photo in hs:
            photo.convert_tags_to_int(tags)    

                        
            
            

        



