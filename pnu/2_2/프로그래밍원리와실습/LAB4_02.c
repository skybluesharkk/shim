#include <stdio.h> 
void print_nxn(int n, double M[n][n]); // Function Declaration

/**
* @brief : Calculating the determinant of a square matrix of order n
* @return: the determinant of M
* @param : n - the order of a square matrix M. M - a 2 dimensional array containing values of a matrix M
*/
double determinant(int n, double M[n][n]) {
if (n==1){
	return M[0][0];
}
else if (n==2){
	return M[0][0]*M[1][1]-M[0][1]*M[1][0];
}else{
double det=0;
int state=1;
for (int i=0;i<n;i++){
  double sub[n-1][n-1];
	int k=0;
	int l=0;
	
	for (int y=0;y<n;y++){
		for(int x=0;x<n;x++){
			if(y!=0 && x!=i){
				sub[k][l]=M[y][x];
				l=(l+1)%(n-1);
				if (l==0) k++;
			}
		}
	}
det =  det+state*determinant(n-1,sub)*M[0][i];
state=state*(-1);
}
return det;
}
}

int main(void) {
	double M1[3][3] = { {1.7, 3.2, 2.5},
			{2.3, 4.1, 0.7},
			{1.0, 2.0, 3.0} };
	double M2[4][4] = { {2.0, 1.0, 2.0, 1.0},
			{1.7, 3.2, 2.5, 3.0},
			{2.3, 4.1, 0.7, 2.0},
			{1.0, 2.0, 3.0, 4.0} };
	// the values of M3 are hidden on purpose
	double M3[5][5] = { {2.0, 1.0, 2.0, 1.0, 0.0},
			{1.7, 3.2, 2.5, 3.0, 1.0},
			{2.3, 4.1, 0.7, 2.0, 0.0},
			{2.3, 4.1, 0.7, 2.0, 0.0},
			{1.0, 2.0, 3.0, 4.0, 1.0} };
	int option;
	
	scanf("%d",&option);
	
	switch (option) {
		case 1 :
			printf("Matrix M1 = \n");
			print_nxn(3, M1);
			printf("det(M1) = %lf\n", determinant(3, M1));
			break;
		case 2 :
			printf("Matrix M2 = \n");
			print_nxn(4, M2);
			printf("det(M2) = %lf\n", determinant(4, M2));
			break;
		default :
			printf("det(M3) = %lf\n", determinant(5, M3));
			break;
	}

	return 0;
}

// print a Square Matrix M of order n
void print_nxn(int n, double M[n][n]) {
	int row, col;
	for (row=0; row<n; row++) {
		printf("    [ ");
		for (col=0; col<n; col++)
			printf("%6.2lf ", M[row][col]);
		printf("]\n");
	}
}
