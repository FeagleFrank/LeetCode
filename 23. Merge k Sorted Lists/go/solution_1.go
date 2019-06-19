package main

//Definition for singly-linked list.
type ListNode struct {
	Val int
	Next *ListNode
}


func mergeKLists(lists []*ListNode) *ListNode {
	var listsNotNil []*ListNode
	for _, v := range lists {
		if v != nil {
			listsNotNil = append(listsNotNil, v)
		}
	}
	var head = &ListNode{0,nil}
	merge(head, listsNotNil)
	return head.Next
}

func merge(chead *ListNode, lists []*ListNode){
	if len(lists) == 0 {
		return
	}
	minPos := 0
	for i:=1;i<len(lists);i++ {
		if lists[i].Val < lists[minPos].Val {
			minPos = i
		}
	}
	chead.Next = lists[minPos]
	if lists[minPos].Next == nil {
		lists = append(lists[:minPos],lists[minPos+1:]...)
	}else{
		lists[minPos] = lists[minPos].Next
	}
	merge(chead.Next, lists)
}

func main() {
	//l1 := generateListNode([]int{1,4,5})
	//l2 := generateListNode([]int{1,3,4})
	//l3 := generateListNode([]int{2,6})
	//merge := mergeKLists([]*ListNode{l1, l2, l3})
	l1 := generateListNode([]int{})
	merge := mergeKLists([]*ListNode{l1})
	printListNode(merge)
}

func generateListNode(n []int) *ListNode{
	var head *ListNode
	var pre *ListNode
	for i, v := range n {
		c := &ListNode{v,nil}
		if i != 0 {
			pre.Next = c
		}else{
			head = c
		}
		pre = c
	}
	return head
}

func printListNode(listNode *ListNode) {
	if listNode == nil{
		print("nil")
		return
	}
	print(listNode.Val)
	if listNode.Next != nil {
		print("->")
		printListNode(listNode.Next)
	}
}


//runtime: 168ms	Memory: 8.8MB
