def search(a,sx,sy,tx,ty):
    a[sx][sy]=1
    q=[(sx,sy)]
    while len(q)!=0:
        fx,fy=q.pop()
        for i,j in kattack(fx,fy):
            if a[i][j]==0:
                a[i][j]=1
                q.insert(0,(i,j))
    return a[tx][ty]

def kattack(i,j):
    g=[(i-2,j-1),(i-2,j+1),(i-1,j-2),(i+1,j-2),(i+2,j-1),(i+2,j+1),(i+1,j+2),(i-1,j+2)]
    p=[]
    for a,b in g:
        if a>=0 and a<r and b>=0 and b<c:
            p.append((a,b))
    return p

r,c=map(int,input().split())
a=[[0 for i in range(c)]for i in range(r)]
sx,sy,tx,ty=map(int,input().split())
print(bool(search(a,sx,sy,tx,ty)))