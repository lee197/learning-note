
# 一般数据格式：

public class Node{
int val;
Node next;
Node(int x) { val = x; }

}
# 删除节点的时候，要找到节点的前一个节点才能做删除操作，必要时可以加dummyhead

deleteNode = p.next
p.next = deleteNode.next
deletNode = None
 

# 反转列表经验：

# 迭代解决方案：

class Solution {
    public ListNode reverseList(ListNode pHead) {

    ListNode prev = null;
    ListNode current = pHead;
    ListNode next = null;

   if (pHead == null || pHead.next == null){
       return pHead;
    }

while(current != null){

next = current.next;// 设置temp就是要把指针缓存下来，因为后面要对current指针做改动
current.next = prev;// current.next = prev 这是改变current.next的值或者内存地址！！！，current= current.next是吧current当前值赋给其他元素
prev = current; //因为这是反转指针，指针的方向是不定的，所以不能用current = current.next 或者 prev = prev.next 来挪动指针
current = next;

    }

return prev;

    }
}
 

# 递归解决方案：
 

# //解决方案为：在层层深度递归的时候，把链表指针打断，层层返回的时候将链表反向接起来
class Solution {
    
    //递归一般是从最多开始，推到最小或者倒数第二小的时候层层返回。
    
    public ListNode reverseList(ListNode pHead) {
        
    if(pHead==null || pHead.next == null){ //如果没有结点或者只有一个结点直接返回pHead，递归的一个退出条件，一般触发一次
        
        return pHead;
    }
        
    ListNode pNext = pHead.next; //保存当前结点的下一结点，由于是递归，这个变量不会被销毁，直到函数的返回语句被执行，所以每块函数的栈内存都会有这个变量，还有其他变量以及其状态
        
    pHead.next = null; //打断当前结点的指针域
        
    ListNode reverseHead = reverseList(pNext); //递归结束时reverseHead一定是新链表的头结点
        
    pNext.next = pHead; //修改指针域
        
    return reverseHead;//这个在递归中层层返回
    }
}
# 删除列表种指定的一个或多个元素（添加元素法）：

class Solution {
    
    # //删除元素的时候，要考虑如果第一个元素是需要删除的元素的情况，这时候就不能把前一个元素的next给当前元素的next了，因为前一个元素是null
    # //所以要添加一个头元素，构造一个新的链表，最后返回新链表的next
    public ListNode removeElements(ListNode head, int val) {
       ListNode result = new ListNode(-1);//创造一个新的链表，目前只有一个元素
        # //把目标链表接上
        result.next=head;
        ListNode current=head,prev=result;//创建一个当前（快），一个之前的指针（慢）
        while(current!=null){
            if(current.val==val){
                prev.next=current.next;//如果遇到了，处理
            }else{
                prev=prev.next;//没遇到就把慢指针移一位
            }
            current=current.next;//每次都会移动快指针
        }
        return result.next;
    }

    }
# 判断是否是回文列表：要求是O（1）空间复杂度，O（n）时间复杂度，

# 思路：找到链表中部节点，反转一半链表，然后与另一半对比

# /**
#  * Definition for singly-linked list.
#  * public class ListNode {
#  *     int val;
#  *     ListNode next;
#  *     ListNode(int x) { val = x; }
#  * }
#  */
class Solution {

    public boolean isPalindrome(ListNode head) {

if (head == null || head.next == null){

return true;
}

ListNode fast = head;
ListNode slow = head;

# //通过快慢指针找到中间位置
while (fast.next != null && fast.next.next != null){

fast = fast.next.next;
slow = slow.next;
}

ListNode firstHalf = head; //把指针返回到第一半链表
ListNode lastHalf = slow.next;
ListNode reversedLastHalf = reverseLinkedList(lastHalf);//反转第二半链表
 
while ( firstHalf != null && reversedLastHalf != null && reversedLastHalf.val == firstHalf.val){

firstHalf = firstHalf.next;
reversedLastHalf = reversedLastHalf.next;
}

return reversedLastHalf == null;// 尽量不要用fisrtHalf == null来判断，有可能两个部分的链接没有被打断，比如[0，0]，在反转的时候直接返回原指针，并没有打断链接
    }
    

# //反转链表
private ListNode reverseLinkedList(ListNode head){

ListNode prev = null;
ListNode current = head;

if (head == null && head.next == null){
        
        return head;
    }
    
while (current != null){

ListNode temp = current.next;
current.next = prev;
prev = current;
current = temp;

}

return prev;

}
}
# 双链表操作：

class ListNode{
int val;

ListNode prev；

ListNode next;

ListNode(int x){

val = x;

}

}

class Solution{
# //获得想要的节点
public ListNode getNode(ListNode head, int index){
if (head == null){//初步判断节点是否在特殊情况
    return null;
}
int k = 0;

while(k < index && head != null){ //通过这种方式找到想要的节点
head = head.next;
k++;
}

if (k == index){

return head.val;
}else{
# //如果k!=index表示index太大没有那么多节点
return null;
}

}

public void addAtHead(ListNode head, int val){

if (head == null){
    return
}

ListNode newNode = new ListNode(val);

if (!node ){
System.out.print("memory issue")
return
}

newNode.next = head;
head.prev = newNode;
newNode.prev = null;

return
}

public void addAtTail(ListNode head,int val){
if (head == null){
    return
}

ListNode newNode = new ListNode(val);

if (!newNode){
    System.out.print("memory issue")
    return;
}

ListNode current = head;

while(current.next != null){
current = current.next
}

current.next = newNode;
newNode.prev = current;
newNode.next = null;
}

public void addAtIndex(ListNode head, int index, int val){
if (head == null){
    return
}

ListNode newNode = new ListNode(val);

if (!newNode){
    System.out.print("memory issue")
    return;
}

int k = 1;
ListNode temp = head;

while (k<index && temp.next != null){

    temp = temp.next;
    k++;
}

if (k!=index){

    System.out.print("cannot find desired node");
}
# //交换思路：先把新的节点连接上，再调整前置与后置节点
newNode.next = temp.next;
newNode.prev = temp;

temp.next = newNode;

if (temp.next != null) {
temp.next.prev = newNode;

}

return;

}

public void deleteAtIndex(ListNode head, index int){
if (head == null){
    return
}

int k = 1;
ListNode temp = head;

while (k<index && temp.next != null){

    temp = temp.next;
    k++;
}

if (k!=index){

System.out.print("cannot find desired node");
}

if (temp.prev != null && temp.next != null){
# //思路：前节点，后节点相互指向对方，再把中间节点置为空
temp.prev.next = temp.next;
temp.next.prev = temp.prev;
temp = null;
}

}
}
