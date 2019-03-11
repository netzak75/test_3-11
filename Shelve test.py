import shelve
with shelve.open('ShelveTest') as fruit:
    fruit['orange'] = "a sweet, orange, citrus fruit"
    fruit['apple'] = "a sweet fruit for making cider"
    fruit['grape'] = "a small, sweet fruit that grows in bunches"
    fruit['banana'] = "a long yellow fruit covered in a peel"
    fruit['cherry'] = "a small, red fruit with a pit in the middle"

    print(fruit["cherry"])
    print(fruit["apple"])
