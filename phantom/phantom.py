import numpy as np


def phantom(npx: int, ellipses: np.array = None):

    # Create blank image
    p = np.zeros((npx, npx))

    # Create the pixel grid
    ygrid, xgrid = np.mgrid[-1:1:(1j * npx), -1:1:(1j * npx)]

    for e in ellipses:
        I = e[0]
        a2 = e[1] ** 2
        b2 = e[2] ** 2
        x0 = e[3]
        y0 = e[4]
        phi = e[5] * np.pi / 180  # Rotation angle in radians

        # Create the offset x and y values for the grid
        x = xgrid - x0
        y = ygrid - y0

        cos_p = np.cos(phi)
        sin_p = np.sin(phi)

        # Find the pixels within the ellipse
        locs = (((x * cos_p + y * sin_p) ** 2) / a2
                + ((y * cos_p - x * sin_p) ** 2) / b2) <= 1

        # Add the ellipse intensity to those pixels
        p[locs] += I

    return p


def create_phantom(n_offsets: int, mvec: np.array, npx: int = 256) -> np.array:
    img_stack = np.zeros([n_offsets, npx, npx])

    for i in range(n_offsets):
        e = [[1, .69, .92, 0, 0, 0],
             [-1, .1600, .4100, -.22, 0, 18],
             [+mvec[i], .1600, .4100, -.22, 0, 18],
             [-1, .1100, .3100, .22, 0, -18],
             [+mvec[i], .1100, .3100, .22, 0, -18]]

        img_stack[i, :, :] = phantom(npx=npx, ellipses=e)
    return img_stack
