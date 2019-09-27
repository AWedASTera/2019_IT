    
import matplotlib.pyplot as plt
import numpy as np


def get_kernel(windos_size, sigma):
    kernel = np.zeros((windos_size, windos_size))
    mid = windos_size//2
    for i in range(windos_size):
        for j in range(windos_size):
            kernel[i, j] = np.exp(-((i-mid) ** 2 + (j-mid) ** 2)/(2*sigma**2))
    kernel/=np.sqrt(2*np.pi)*sigma
    return kernel


def filter(img, window_size, sigma):
    img2 = np.zeros_like(img)
    p = window_size//2
    kernel = get_kernel(window_size, sigma)
    for k in range(img.shape[2]): # foreach color channel
        for i in range(p, img.shape[0]-p): # foreach row
            for j in range(p, img.shape[1]-p): # foreach column
                window = img[i-p:i+p+1, j-p:j+p+1, k]
                img2[i,j,k] = (kernel*window).sum()
    return img2


def main():
    img = plt.imread("img.png")[:, :, :3]
    w_size = int(input("Input window size: "))
    sigma = int(input("Input degree of blur: "))
    img2 = filter(img, w_size, sigma)
    fig, axs = plt.subplots(1,2)
    axs[0].imshow(img)
    axs[1].imshow(img2)
    plt.show()


if __name__ == "__main__":
    main()