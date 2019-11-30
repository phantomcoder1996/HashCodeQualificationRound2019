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


def convert_vertical_to_horizontal(vs):

    horizontal_photos = []
    is_selected= dict([(v.id,False) for v in vs])
   
    new_id = 0

    for photo1 in vs:
        if not is_selected[photo1.id]:
            best_comb = None
            best_comb_phs = None
            sol_exists = False
            num_tags = -1
            # find the photo that maximizes the combined number of tags in two photos
            for photo2 in vs:
                if photo2.id != photo1.id and not is_selected[photo2.id]:
                    x = np.union1d(photo1.tags,photo2.tags)
                    if  x.shape[0] > num_tags:
                        num_tags = x.shape[0]
                        best_comb = x
                        best_comb_phs = (photo1,photo2)
                        sol_exists = True
            if sol_exists:
                p1 = best_comb_phs[0]
                p2 = best_comb_phs[1]
                is_selected[p1.id] = True
                is_selected[p2.id] = True
                horizontal_photos.append(slide(new_id,best_comb,"H"))
                new_id += 1
    
    return horizontal_photos



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--infile","-i",default="c_memorable_moments.txt")
    parser.add_argument("--outfile","-o",default='out.txt')

    args = parser.parse_args()
    infile = args.infile
    outfile = args.outfile


    vs = []
    hs = []
    all_photos = []
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

        converted_vs = convert_vertical_to_horizontal(vs)

        print("total number of converted photos = {} ".format(len(converted_vs)))

        all_photos = hs + converted_vs # you should work on this array
        print("total number of photos = {} ".format(len(all_photos)))


        # solution code


        # write output
        
        with open(outfile,"w") as f:
            f.write("solution\n")


                        
            
            

        



