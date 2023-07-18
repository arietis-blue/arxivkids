import Mock from 'mockjs'

Mock.mock('/api/users', 'post', {
    'users|5': [
      {
        'id|+1': 1,
        'name': '@name',
        'age|18-60': 1
      }
    ]
  })