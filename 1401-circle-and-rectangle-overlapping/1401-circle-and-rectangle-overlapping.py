class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        # points = []

        
        # for x in range(x1, x2 + 1):
        #     for y in range(y1, y2 + 1):
        #         points.append((x, y))

        # # Har point ko circle se check karo
        # for x, y in points:

        #     distance = (x - xCenter) ** 2 + (y - yCenter) ** 2

        #     if distance <= radius ** 2:
        #         return True

        # return False
        # class Solution(object):
        #     def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
     
        

        
        # points = [(x1,y1) , (x2,y2)]
        

        # for z in range(x1+1,x2):
            
        #     for k in range(y1+1,y2):
        #         points.append((z,k))
        
        # for x , y in points:
        #     if (x - xCenter ) ** 2 + (y- yCenter)**2 <= radius**2:
        #         return True
        #         
        # return False

        closestX = max(x1,min(xCenter,x2))
        closestY = max(y1,min(yCenter,y2))

        distance = (closestX - xCenter)**2+ (closestY - yCenter)**2

        return distance <= radius **2


