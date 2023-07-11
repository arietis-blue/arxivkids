import Mock from 'mockjs'
const Random = Mock.Random

Mock.mock('api/papers/getBody', (req, res) => { //当post或get请求到/api/users/路由时Mock会拦截请求并返回上面的数据
    let body = "あぁ〜〜よしゃいくぞ"
    return body
})


Mock.mock('api/papers/getKeywords', (req, res) => { //当post或get请求到/api/users/路由时Mock会拦截请求并返回上面的数据
    let a = ["tiger", "fire"]
    return a
})