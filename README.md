<div align="center">

# Effective-Python

_Algebraic effects similar to declarative expressions in Python._

> 头顶的星辰便是梦的信标

</div>

灵感来自于 [Algebraic Effects for the Rest of Us](https://overreacted.io/algebraic-effects-for-the-rest-of-us/)

## 对照

```js
function getName(user) {
  let name = user.name;
  if (name === null) {
  	name = perform 'ask_name';
  }
  return name;
}

function makeFriends(user1, user2) {
  user1.friendNames.push(getName(user2));
  user2.friendNames.push(getName(user1));
}

const arya = { name: null, friendNames: [] };
const gendry = { name: 'Gendry', friendNames: [] };
try {
  makeFriends(arya, gendry);
} handle (effect) {
  if (effect === 'ask_name') {
  	resume with 'Arya Stark';
  }
}
```

```python
class User:
    def __init__(self, name = None):
        self.name = name

def getName(user):
    name = user.name
    if name:
        name = Effective.perform('ask_name')
    return name

def makeFriends(user1, user2):
    print(getName(user1))
    print(getName(user2))


def main():
    arya = User()
    gendry = User('Gendry')
    effective = Effective(ask_name = lambda : 'Arya Stark')
    makeFriends(arya, gendry)

main()
```

## 使用

* 通过 `Effective` 实例化一个对象, 并保存在当前命名空间

> effective = Effective()

* 通过 `Effective.perform` 获取代数效应

> Effective.perform('')

## 优先级

通过调用栈回溯, 寻找最近声明的 `Effective` 实例, 如果没有被当前 `Effective` 代数效应捕获, 则继续回溯.

## 参考

[example](./example)
