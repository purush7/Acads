package pplAssignment

object F2016A7PS0025P{
    //Dot product
	def dotProduct(kernel1:List[List[Double]],kernel2:List[List[Double]]):Double ={
		def product(t1:List[Double],t2:List[Double]):Double ={
		if(t1.isEmpty)0
		else{
			t1.head*t2.head + product(t1.tail,t2.tail)
			}
		}
		if(kernel1.isEmpty)0
		else{
			product(kernel1.head,kernel2.head) + dotProduct(kernel1.tail,kernel2.tail)
			}
		
	}
    //convolution
	def convolute(image:List[List[Double]],kernel1:List[List[Double]],imagesize:List[Int],kernel1size:List[Int]):List[List[Double]] = {
	val c =1
	val r =1
		def func2(r:Int,c:Int,image:List[List[Double]],kr:Int,kc:Int,ic:Int,ir:Int,kernel1:List[List[Double]]):List[List[Double]] ={
			def create_matrix(c:Int,image:List[List[Double]],kr:Int,kc:Int,ic:Int,kernel1:List[List[Double]]):List[Double] ={
				def func1(c:Int,image:List[List[Double]],kr:Int,kc:Int):List[List[Double]] ={
					def row(list:List[Double],c:Int,kc:Int):List[Double] ={
						def skipcol(list:List[Double],c:Int):List[Double] ={
						if(list.nonEmpty){
						if(c > 1)skipcol(list.tail,c-1)
						else list}
						else Nil
						}
						def takekc(list:List[Double],k_c:Int):List[Double] ={
						if(list.nonEmpty){
						if(k_c>0)list.head::takekc(list.tail,k_c-1)
						else Nil}
						else Nil
						}
					takekc(skipcol(list,c),kc)
					}
				if(image.nonEmpty){
					if(kr>1)row(image.head,c,kc)::func1(c,image.tail,kr-1,kc)
					else row(image.head,c,kc)::Nil}
				else Nil
				}
			if(c<ic-kc+1)dotProduct(func1(c,image,kr,kc),kernel1)::create_matrix(c+1,image,kr,kc,ic,kernel1)
			else dotProduct(func1(c,image,kr,kc),kernel1)::Nil
			}
		
			def skiprow(image:List[List[Double]],r:Int):List[List[Double]] ={
			if(r>1&&image.nonEmpty)skiprow(image.tail,r-1)
			else image
			}
			if(r<ir-kr+1)create_matrix(c,image,kr,kc,ic,kernel1)::func2(r+1,c,skiprow(image,2),kr,kc,ic,ir,kernel1)
			else create_matrix(c,image,kr,kc,ic,kernel1)::Nil
		}
	func2(r,c,image,kernel1size.head,(kernel1size.tail).head,(imagesize.tail).head,imagesize.head,kernel1)
	}

    //activation
	def activationLayer(activationFunc:Double => Double,image:List[List[Double]]):List[List[Double]] = {
		def act(activationFunc:Double => Double,x:List[Double]):List[Double] = {
		if(x.isEmpty)Nil
		else activationFunc(x.head)::act(activationFunc,x.tail)
		}
		if(image.isEmpty)Nil
		else act(activationFunc,image.head)::(activationLayer(activationFunc,image.tail))
	}

    //single pooling
	def singlePooling(max:List[Double]=>Double,poolmat:List[List[Double]],size:Int):List[Double] = {
	val c = 1
		def pool(max:List[Double]=>Double,poolmat:List[List[Double]],size:Int):List[Double] = {
			def func1(poolmat:List[List[Double]],size:Int):List[Double] ={
				def takekc(list:List[Double],k_c:Int):List[Double] ={	
				if(list.nonEmpty){		
				if(k_c>0)list.head::takekc(list.tail,k_c-1)
				else Nil}
				else Nil
				}
			if(poolmat.nonEmpty){	
				if((poolmat.tail).nonEmpty) takekc(poolmat.head,size):::func1(poolmat.tail,size)
				else takekc(poolmat.head,size)
				}
			else Nil
			}
			def reset(poolmat:List[List[Double]],size:Int):List[List[Double]] ={
				def row(list:List[Double],size:Int) ={
					def skipcol(list:List[Double],c:Int):List[Double] ={
					if(list.nonEmpty){
					if(c > 0)skipcol(list.tail,c-1)
					else list}
					else Nil
					}
				skipcol(list,size)
				}
			if((poolmat.tail).nonEmpty) row(poolmat.head,size)::reset(poolmat.tail,size)
			else row(poolmat.head,size)::Nil
			}
		if(poolmat.isEmpty)Nil
		else {
		if((reset(poolmat,size).head).nonEmpty) {max(func1(poolmat,size))::pool(max,reset(poolmat,size),size)}
		else max(func1(poolmat,size))::Nil}
		}
	if(poolmat.isEmpty)Nil
	else pool(max,poolmat,size)
	}

    //pooling
	def poolingLayer(max:List[Double]=>Double,image:List[List[Double]],size:Int):List[List[Double]] = {
		def reset(image:List[List[Double]],size:Int):List[List[Double]] ={
		if(size >0) reset(image.tail,size-1)
		else image
		}
		def cutter(image:List[List[Double]],size:Int):List[List[Double]] ={
		if(size >0) image.head :: cutter(image.tail,size-1)
		else Nil
		}
	if(reset(image,size).nonEmpty) singlePooling(max,cutter(image,size),size)::poolingLayer(max,reset(image,size),size)
	else singlePooling(max,cutter(image,size),size)::Nil

	}

    //Normalize
	def normalise(nmat:List[List[Double]]):List[List[Int]] = {
		def func1(nmat:List[List[Double]],min:Double,max:Double):List[List[Int]] = {
			def row(t1:List[Double],min:Double,max:Double):List[Int] ={
			if(t1.isEmpty)Nil
			else{
				normalizefn(t1.head,min,max)::row(t1.tail,min,max)
				}
			}
			if(nmat.isEmpty)Nil
			else{
				row(nmat.head,min,max) :: func1(nmat.tail,min,max)
				}
		}
		func1(nmat,(minmaxcol(nmat,(nmat.head).head::(nmat.head).head::Nil)).head,(minmaxcol(nmat,(nmat.head).head::(nmat.head).head::Nil).tail).head)
	}

    //minmax
	def minmaxcol(matrix:List[List[Double]],list2:List[Double]):List[Double] ={
		def minmaxrow(list1:List[Double],list2:List[Double]):List[Double] ={
			if(list1.nonEmpty){
		 		if(list2.head>list1.head){
					if((list2.tail).head<list1.head) minmaxrow(list1.tail,list1.head::list1.head::Nil)
					else minmaxrow(list1.tail,list1.head::list2.tail)
					}
				else	{
					if((list2.tail).head<list1.head) minmaxrow(list1.tail,list2.head::list1.head::Nil)
					else minmaxrow(list1.tail,list2)
					}
			}
			else list2
		}
		if(matrix.nonEmpty){
	 		if(list2.head>minmaxrow(matrix.head,list2).head){
				if((list2.tail).head<(minmaxrow(matrix.head,list2).tail).head) 
					minmaxcol(matrix.tail,minmaxrow(matrix.head,list2).head::(minmaxrow(matrix.head,list2).tail).head::Nil)
				else minmaxcol(matrix.tail,minmaxrow(matrix.head,list2).head::list2.tail)
				}
			else	{
				if((list2.tail).head<(minmaxrow(matrix.head,list2).tail).head) 
					minmaxcol(matrix.tail,list2.head::(minmaxrow(matrix.head,list2).tail).head::Nil)
				else minmaxcol(matrix.tail,list2)
				}
		}
		else list2
	}
     // normalizefn
	def normalizefn(x:Double,min:Double,max:Double):Int ={
		((((x-min)/(max-min))*255.0).toFloat).round

	}
 

    //mixed layer
	def mixedLayer(image:List[List[Double]],kernel1:List[List[Double]],imagesize:List[Int],kernel1size:List[Int],activationFunc:Double => Double,poolingFunc:List[Double]=>Double,size:Int):List[List[Double]] ={
		
		poolingLayer(poolingFunc,activationLayer(activationFunc,convolute(image,kernel1,imagesize,kernel1size)),size)
	}


    //assembly layer
	def assembly(image:List[List[Double]],imagesize:List[Int],w1:Double,w2:Double,b:Double,kernel1:List[List[Double]],kernel1size:List[Int],kernel2:List[List[Double]],kernel2size:List[Int],kernel3:List[List[Double]],kernel3size:List[Int],size:Int):List[List[Int]] ={
		val t1 = mixedLayer(image,kernel1,imagesize,kernel1size,(x:Double)=>if(x>0) x else 0,avg,size)
		val t2 = mixedLayer(image,kernel2,imagesize,kernel2size,(x:Double)=>if(x>0) x else 0,avg,size)
		val t3 = add(t1,t2,w1,w2,b)
		val t4 = mixedLayer(t3,kernel3,((imagesize.head-kernel1size.head+1)/size)::(((imagesize.tail).head-(kernel1size.tail).head+1)/size)::Nil,kernel3size,(x:Double)=>if(x>0) x else 0.5*x,max,size)

		normalise(t4)
		
	}
    // max
	def max(xs: List[Double]): Double = {
		if(xs.tail.nonEmpty){
			val tl = max(xs.tail)
      			if(tl > xs.head) tl
			else xs.head
			}else{
			xs.head
			}
 	}
    // avg
	def avg(x: List[Double]): Double = {
		def fn(x: List[Double],y:Double,z:Int):Double ={
			if(x.nonEmpty) fn(x.tail,(y*z + x.head)/z+1,z+1)
			else y
		}
	fn(x,x.head,1)
 	}

	def add(t1:List[List[Double]],t2:List[List[Double]],w1:Double,w2:Double,b:Double):List[List[Double]]= {	
		def row(l1:List[Double],l2:List[Double],w1:Double,w2:Double,b:Double):List[Double] ={
		if(l1.isEmpty)Nil
		else{
			(l1.head+l2.head+b)::row(l1.tail,l2.tail,w1,w2,b)
			}
		}
		if(t1.nonEmpty)
		row(t1.head,t2.head,w1:Double,w2:Double,b:Double)::add(t1.tail,t2.tail,
		w1:Double,w2:Double,b:Double)
		else Nil
	}

}
