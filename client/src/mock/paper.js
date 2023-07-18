import Mock from 'mockjs'
const Random = Mock.Random

// const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay))

Mock.mock('api/papers/getBody', (req, res) => { //当post或get请求到/api/users/路由时Mock会拦截请求并返回上面的数据
    // await new Promise(resolve => setTimeout(resolve, 5000));
    // let body = "あぁ〜〜よっしゃいくぞ"
    // return body
    // await sleep(1000)
    return "あぁ〜〜よっしゃいくぞ"
})


Mock.mock('api/paper/getKeywords', (req, res) => { //当post或get请求到/api/users/路由时Mock会拦截请求并返回上面的数据
    let a = ["tiger", "fire"]
    return a
})