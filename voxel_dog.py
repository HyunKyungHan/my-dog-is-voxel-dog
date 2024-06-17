import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure(figsize=(9,9))

ax = fig.add_subplot(projection='3d')
dimensions = (45,45,45)

voxels = np.full(dimensions, False)

# front legs
voxels[13:17, 10:16, 0:2], voxels[20:24, 10:16, 0:2] = True, True
voxels[13:17, 14:16, 2:8], voxels[20:24, 14:16, 2:8] = True, True
voxels[13:17, 12:14, 2:18], voxels[20:24, 12:14, 2:18] = True, True
voxels[17:20, 13:15, 11:18], voxels[17:20, 12:15, 13:18] = True, True
# back legs
voxels[13:17, 24:28, 0:2], voxels[20:24, 24:28, 0:2] = True, True
voxels[13:17, 26:30, 0:8], voxels[20:24, 26:30, 0:8] = True, True
# body
voxels[13:24, 16:29, 7:8] =  True
voxels[13:24, 14:30, 8:9] =  True
voxels[13:24, 14:31, 9:10] =  True
voxels[13:24, 14:32, 10:15] =  True
voxels[13:24, 14:31, 15:16] =  True
voxels[13:24, 14:30, 16:17] =  True
voxels[13:24, 14:29, 17:18] =  True
# tail
voxels[18:21, 30:32, 15:17] =  True
voxels[18:21, 32:34, 17:19] =  True  
voxels[18:21, 33:35, 19:21] =  True
voxels[18:21, 34:36, 21:25] =  True
voxels[18:21, 32:35, 25:27] =  True
# face
voxels[13:24, 12:20, 18:20] =  True
voxels[13:24, 12:18, 18:22] =  True
voxels[14:23, 10:16, 22:23] =  True
voxels[14:23, 7:14, 23:25] =  True
voxels[16:23, 5:14, 25:28] =  True
voxels[16:23, 6:14, 27:38] =  True # increase head size
voxels[16:23, 5:14, 28:38] =  True # head
voxels[16:23, 2:5, 28:32] =  True # mouth
voxels[19:21, 0:2, 30:32] =  True # nose
voxels[15:16, 9:13, 34:42], voxels[23:24, 9:13, 34:42] =  True, True # outer ears
voxels[16:17, 9:13, 38:42], voxels[22:23, 9:13, 38:42] =  True, True # inner ears
voxels[17:18, 4:5, 32:34], voxels[21:22, 4:5, 32:34] =  True, True # eyes
voxels[15:22, 11:12, 17:20], voxels[14:23, 10:12, 19:22]=  True, True

ax.voxels(voxels)
# ax.axis('off')
ax.set_title('Voxel Dog')