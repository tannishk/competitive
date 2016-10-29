object Main extends App {

  abstract class LinkedList
  case class Node(value: Int, next: LinkedList) extends LinkedList
  case class Tail(value: Int) extends LinkedList

  def getLengthOfLinkedList(list: LinkedList): Int = {
    def traverseList(remainder: LinkedList, length: Int): Int = remainder match {
      case node: Node => traverseList(node.next, length + 1)
      case _: Tail => length + 1
    }
    traverseList(list, 0);
  }

  val linkedList = new Node(
    0, new Node(
      1, new Node(
        2, new Node(
          3, new Tail(4)
        )
      )
    )
  )

  println(getLengthOfLinkedList(linkedList))
}