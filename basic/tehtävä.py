#partOne

def cal_wrapping(dimensions):
         total_wrapping = 0
         for l,w,h  in dimensions:
            surface = (2*l*w) + (2*w*h) + (2*h*l)  #method of counting surface without edge
               #counting lower edge
            if (l*w)<(w*h) &(l*w)<(h*l):
                   lower_edge = l*w
            if (w*h)<(l*w) & (w*h)<(h*l):
                     lower_edge = w*h
            else:
                lower_edge = h*l
                #lower_edge = min((l*w),(w*h),(ç )
                total_wrapping += surface + lower_edge
      
         return total_wrapping
#partTwo calculating ribbon

def cal_ribbon(dimensions):
         total_ribbon = 0
         for l,w,h  in dimensions:
             smallest_perimeter = 2 * (l + w + h - max(l, w, h))
               # Ribbon for the bow (volume of the box)
             bow_ribbon = l * w * h
        # Total ribbon for this box
             total_ribbon += smallest_perimeter + bow_ribbon
      
             return total_ribbon
            
                
  

dimensions = []
print('enter the number of boxes')
num_of_box = int(input())
for i in range(num_of_box):
    print(f'enter the edges of the boxex {i +1} (length width height) ')
      #input into list with split function
    l,w,h = map(int,input().split())
      #append funtion added the converted input to the dimension list
    dimensions.append((l,w,h))


needed_wrapping = cal_wrapping(dimensions)
needed_ribbon = cal_ribbon(dimensions)
print(f'We need to order {needed_wrapping} squire feet wrapping paper for the boxes')
print(f'We need to order {needed_ribbon} squire feet wrapping paper for the boxes')