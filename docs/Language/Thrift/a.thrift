struct User {
	1: required i32 id;
	2: required string name;
}

service UserServer {
	User getUser(1: string userid);
}
