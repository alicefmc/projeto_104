import cv2

img = cv2.imread("solar-system.jpg") 
cv2.putText(img,
            "Sol",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Mercurio",
            (100,190),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "Venus",
            (190,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "Terra",
            (290,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "Marte",
            (390,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "Jupiter",
            (490,80),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "Saturno",
            (690,115),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "Urano",
            (925,125),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "Neturno",
            (1090,125),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )
cv2.imwrite("Solar_systemwithname.jpg",img)
cv2.imshow("resultado",img)
cv2.waitKey(0)