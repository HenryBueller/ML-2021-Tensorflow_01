'''

scp -P 29122 -r D:/Afile/exp_3_1_vgg/stu_upload root@120.236.247.203:/opt/code_chap_2_3/code_chap_2_3_student/exp_3_1_vgg

ejzvsfhvmain

cd /opt/code_chap_2_3/code_chap_2_3_student
source env.sh
cd exp_3_1_vgg
python main_exp_3_1.py

 File "/opt/code_chap_2_3/code_chap_2_3_student/exp_3_1_vgg/stu_upload/layers_2.py", line 44, in forward
    input_mat = np.matmul(input_temp, self.weight).sum(axis=(0, 1, 2))
ValueError: operands could not be broadcast together with remapped shapes [original->remapped]: (1,64,3,3)->(1,64,newaxis,newaxis) (64,3,3,64)->(64,3,newaxis,newaxis) and requested shape (3,64)


'''
