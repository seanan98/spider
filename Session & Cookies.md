## 静态网页和动态网页

我们把html文件放在某台具有固定公网IP的主机上，主机上装有Apache或Nginx等服务器，那么这台主机就可以作为服务器，其他人便可以通过访问服务器看到这个页面，这样就搭建了一个最简单的网站。

网页的内容是由HTML代码编写的，文字、图片等内容均通过写好的HTML代码指定，这种网页叫做静态网页，这种网页加载速度快，编写简单。但是可维护性差，不能根据URL灵活多变地显示内容。

动态网页则可以动态解析URL中参数的变化，关联数据库并呈现不同的界面。不再是一个简单的HTML文件。

此外动态网页还可以实现用户登录和注册的功能，很多页面是需要登录才能查看的，按照一般的逻辑，输入用户名和密码后，肯定是拿到了一种类似凭证的东西，有了它我们才能保持登陆状态。

这种凭证就是session和cookies共同产生的结果。

## 无状态HTTP

HTTP协议对事务处理是没有记忆能力的，也就是说服务器不知道客户端是什么状态。当我们向服务器发送请求，服务器会解析此请求，并返回给我们，但是发送和返回是相互独立的，服务器不会记录前后状态的变化。如果后续还需要处理前面的信息，则必须重传，即需要额外传递一些前面的重复请求才能获取后续响应。

为了保持前后状态，用于保持HTTP链接状态的session和cookies就出现了。session在服务器端，cookies在客户端。

## Session

中文称之为会话，在web中，session对象用来存储特定用户session需要的属性以及配置信息。当用户在应用程序的web页之间跳转时，存储在session对象中的变量不会丢失，当session过期或被放弃时，服务器将终止该session。

## Cookies

网站为了辨别用户身份，进行session跟踪而存储在用户本地终端上的数据。

### Session维持

那么，我们怎样利用 Cookies 保持状态呢？当客户端第一次请求服务器时，服务器会返回一个响应头中带有 Set-Cookie 字段的响应给客户端，用来标记是哪一个用户，客户端浏览器会把 Cookies 保存起来。当浏览器下一次再请求该网站时，浏览器会把此 Cookies 放到请求头一起提交给服务器，Cookies 携带了 Session ID 信息，服务器检查该 Cookies 即可找到对应的 Session 是什么，然后再判断 Session 来以此来辨认用户状态。

在成功登录某个网站时，服务器会告诉客户端设置哪些 Cookies 信息，在后续访问页面时客户端会把 Cookies 发送给服务器，服务器再找到对应的 Session 加以判断。如果 Session 中的某些设置登录状态的变量是有效的，那就证明用户处于登录状态，此时返回登录之后才可以查看的网页内容，浏览器再进行解析便可以看到了。

反之，如果传给服务器的 Cookies 是无效的，或者 Session 已经过期了，我们将不能继续访问页面，此时可能会收到错误的响应或者跳转到登录页面重新登录。

所以，Cookies 和 Session 需要配合，一个处于客户端，一个处于服务端，二者共同协作，就实现了登录 Session 控制。

### 属性结构

接下来，我们看看cookie中有哪些内容。

![img](https://s0.lgstatic.com/i/image3/M01/6E/54/CgpOIF5fSryAMaivAANBRdQDiCI200.jpg)

- Name，即该 Cookie 的名称。Cookie 一旦创建，名称便不可更改。
- Value，即该 Cookie 的值。如果值为 Unicode 字符，需要为字符编码。如果值为二进制数据，则需要使用 BASE64 编码。
- Max Age，即该 Cookie 失效的时间，单位秒，也常和 Expires 一起使用，通过它可以计算出其有效时间。Max Age 如果为正数，则该 Cookie 在 Max Age 秒之后失效。如果为负数，则关闭浏览器时 Cookie 即失效，浏览器也不会以任何形式保存该 Cookie。
- Path，即该 Cookie 的使用路径。如果设置为 /path/，则只有路径为 /path/ 的页面可以访问该 Cookie。如果设置为 /，则本域名下的所有页面都可以访问该 Cookie。
- Domain，即可以访问该 Cookie 的域名。例如如果设置为 .zhihu.com，则所有以 zhihu.com，结尾的域名都可以访问该 Cookie。
- Size 字段，即此 Cookie 的大小。
- Http 字段，即 Cookie 的 httponly 属性。若此属性为 true，则只有在 HTTP Headers 中会带有此 Cookie 的信息，而不能通过 document.cookie 来访问此 Cookie。
- Secure，即该 Cookie 是否仅被使用安全协议传输。安全协议。安全协议有 HTTPS、SSL 等，在网络上传输数据之前先将数据加密。默认为 false。

### 会话Cookie和持久Cookie

会话cookie就是把cookie放在浏览器内存中，浏览器关闭cookie失效；

持久cookie则保存在客户端的硬盘，下次继续可以使用。

其实是由cookie的max age/expires字段定义过期时间。

## 常见误区

- “只要浏览器关闭，session就消失了”，❌
- 其实服务器根本不会知道浏览器是否关闭 :+1:
- 之所以有这种错觉，是因为大多数网站使用会话cookie保存session id。如果将session id保存到硬盘上，或者将cookies发送给服务器，则再次打开浏览器，仍然可以找到原来的session id。
- 恰恰是由于浏览器关闭不会导致session被删除，这就需要服务器为session设置一个失效时间。

