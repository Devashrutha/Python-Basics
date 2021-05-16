def linear_search(arr,key):
    for indx,num in enumerate(arr):
        if num==key:
            return indx
    return "Key not found"

key=4
indx=linear_search([2,5,3,4,7,9,0],key)
print(indx)