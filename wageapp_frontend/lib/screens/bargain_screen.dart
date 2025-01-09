import 'package:flutter/material.dart';

class BargainScreen extends StatefulWidget {
  final String workerName;

  BargainScreen({required this.workerName});

  @override
  _BargainScreenState createState() => _BargainScreenState();
}

class _BargainScreenState extends State<BargainScreen> {
  final TextEditingController _offerController = TextEditingController();
  String? workerResponse;

  void sendOffer() {
    setState(() {
      workerResponse = "Worker responded: \$${int.parse(_offerController.text) + 50}";
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Bargain with ${widget.workerName}'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Enter your offer for ${widget.workerName}:',
                style: TextStyle(fontSize: 18)),
            SizedBox(height: 10),
            TextField(
              controller: _offerController,
              keyboardType: TextInputType.number,
              decoration: InputDecoration(
                border: OutlineInputBorder(),
                hintText: 'Enter your offer in \$',
              ),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: sendOffer,
              child: Text('Send Offer'),
            ),
            if (workerResponse != null) ...[
              SizedBox(height: 20),
              Text(workerResponse!, style: TextStyle(fontSize: 16, color: Colors.green)),
            ]
          ],
        ),
      ),
    );
  }
}
