const express = require('express');
const mysql = require('mysql2');
const cors = require('cors')

// 创建Express
const app = express();
const port = 5000;

app.use(cors());

// 配置MySQL连接池
const pool = mysql.createPool({
  connectionLimit: 10,
  host: '*****',
  port: '*****',
  user: '*****',
  password: '*****',
  database: '*****'
});

// 测试数据库连接
pool.getConnection((err, connection) => {
  if (err) {
    console.error('❌ MySQL Connect Faild', err);
    return;
  }
  console.log(' ✅ MySQL Connect Succeed');
  connection.release(); // 释放连接
});

// 创建路由处理根路径请求
app.get('/api/data', async (req, res) => {
  try {
    // 查询
    const results = await new Promise((resolve, reject) => {
      pool.query('SELECT * FROM summary_mon', (error, results) => {
        if (error) reject(error);  
        resolve(results);
      });
    });
    res.json(results); //返回JSON格式数据

  } catch (error) {
    console.error('查询失败:', error);
    res.status(500).send('服务器内部错误');
  }
});

// 启动服务器
app.listen(port, () => {
  console.log(`服务器运行在 http://localhost:${port}`);
});