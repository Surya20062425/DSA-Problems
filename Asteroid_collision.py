class Solution:

    # we have created a class
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        #  we have created an array asteroid 

        # we have created an other array that stores result
        
        res = []

        for a in asteroids:

            # iterating the loop

            while res and a < 0 < res[-1]:
                # while loop runs after condition is satisfiefd
                if -a > res[-1]:

                    # checking the conditon 

                    # where as it revelas if the two elements are in opposite direction 

                    # the two elements are poped
                    res.pop()
                    continue
                elif -a == res[-1]:

                    # ckeck the condition 

                    # If the both elements are of same size 

                    # both the elements are removed from the array
                    res.pop()
                break
            else:
                res.append(a)

        # if  the elements are not satisfied the both conditions 

        # the remaining elements are appended in the new array ans 

        return res
