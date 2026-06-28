class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for img in image:
            img.reverse()
            for i in range(len(img)):
                img[i] = img[i] ^1
               
        return image
