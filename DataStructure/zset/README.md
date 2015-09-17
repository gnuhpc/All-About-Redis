Sorted Set的实现是hash table(element->score, 用于实现ZScore及判断element是否在集合内)，和skip list(score->element,按score排序)的混合体。 skip list有点像平衡二叉树那样，不同范围的score被分成一层一层，每层是一个按score排序的链表。

ZAdd/ZRem是O(log(N))，ZRangeByScore/ZRemRangeByScore是O(log(N)+M)，N是Set大小，M是结果/操作元素的个数。可见，原本可能很大的N被很关键的Log了一下，1000万大小的Set，复杂度也只是几十不到。当然，如果一次命中很多元素M很大那谁也没办法了。
