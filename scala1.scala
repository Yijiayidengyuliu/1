
object a {
  def main(args: Array[String]) {
    var a=List(31,33,37,30,27,34,31)
    for (i<-Range(0,7)){
        println("星期"+(i+1)+"的温度："+a(i)+"°")
  }
  }
}
