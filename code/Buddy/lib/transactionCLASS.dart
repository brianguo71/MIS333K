class TransactionClass {
  int id;
  String category;
  double val;
  String time;

  TransactionClass(this.id, this.category, this.val, this.time);



  Map<String, dynamic> toMap() {
    var map = <String, dynamic>{
      'id': id,
      'category': category,
      'val': val,
      'time': time
    };
    return map;
  }

  TransactionClass.fromMap(Map<String, dynamic> map) {
    id = map['id'];
    category = map['category'];
    val = map['val'];
    time = map['time'];
  }
}
