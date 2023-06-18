class Entity {
	int x, y;
	int speed;
	virtual std::string interface1() = 0;
	virtual void printf();
};

class Person : public Entity {
private:
 	std::string msg = "asdc";
public:
	std::string interfece1 override {
		return msg;
	};
};