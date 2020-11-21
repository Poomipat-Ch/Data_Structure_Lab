
def weight_box(item_arr, box_count):
    if box_count == 1:
        return sum(item_arr)

    def find_min_weight(index = 0,min_weight=99999999):
        if len(item_arr[index:]) < box_count - 1:
            return min_weight
        
        current_box = sum(item_arr[:index])
        other_box = weight_box(item_arr[index:],box_count-1)

        min_weight = min(max(current_box,other_box), min_weight)

        if index < len(item_arr):
           min_weight = find_min_weight(index+1,min_weight)

        return min_weight
    
    return find_min_weight()






item_arr, box_count = input('Enter Input : ').split('/')
item_arr = list(map(int,(item_arr.split())))
box_count = int(box_count)
print(f"Minimum weigth for {box_count} box(es) = {weight_box(item_arr, box_count)}")
