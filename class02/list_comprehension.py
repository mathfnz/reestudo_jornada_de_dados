# %%
nums: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# nums_quad:list = []

# for num in nums:
#     square = num ** 2
#     nums_quad.append(square)
# print(nums_quad)
 
nums_quad = [num ** 2 for num in nums]
print(nums_quad)

#%%
result = [num for num in nums if num % 2 == 0]
print(result)