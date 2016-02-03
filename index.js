function execute(func) {
    func();
    console.log('executed function');
}

var func = function () {
    console.log('yolo');
};

execute(func);