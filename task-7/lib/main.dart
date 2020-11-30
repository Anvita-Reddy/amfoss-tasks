import 'dart:io';

import 'package:app_Blue/data/data.dart';
import 'package:flutter/material.dart';

void main(){
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "App Blue",
      home: Home() ,
      debugShowCheckedModeBanner: false,
    );
  }
}

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {

  List<SliderModel> slides = new List<SliderModel>();
  int currentIndex = 0;
  PageController pageController = new PageController(initialPage: 0);

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    slides = getSlides();
  }

  Widget pageIndexIndicator(bool isCurrentPage){
    return Container(
      margin: EdgeInsets.symmetric(horizontal: 2.0),
      height: isCurrentPage ? 10.0 : 6.0,
      width: isCurrentPage ? 10.0 : 6.0,
      decoration: BoxDecoration(
        color: isCurrentPage? Colors.deepPurple : Colors.deepPurpleAccent,
        borderRadius: BorderRadius.circular(12)
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: PageView.builder(
        controller: pageController,
        itemCount: slides.length,
          onPageChanged: (val) {
            setState(() {
              currentIndex = val;
            });
          },
          itemBuilder: (context, index){
          return SliderTile(
            imageAssetPath: slides[index].getImageAssetPath(),
            title: slides[index].getTitle(),
            desc: slides[index].getDesc(),
          );
    }),
    bottomSheet: currentIndex != slides.length - 1 ? Container(
      height: Platform.isIOS ? 70 : 60,
      padding: EdgeInsets.symmetric(horizontal: 20),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          GestureDetector(
            onTap: (){
              pageController.animateToPage(slides.length - 1, duration: Duration(milliseconds: 400), curve: Curves.linear);
            },
              child: Text("SKIP")
          ),
          Row(
            children: [
              for(int i=0; i<slides.length; i++) currentIndex == i ?pageIndexIndicator(true) : pageIndexIndicator(false)
            ],
          ),
          GestureDetector(
              onTap: (){
                pageController.animateToPage(currentIndex + 1, duration: Duration(milliseconds: 400), curve: Curves.linear);
              },
              child: Text("NEXT")
          ),
        ],
      ),
    ) : Container(
      alignment: Alignment.center,
      width: MediaQuery.of(context).size.width,
      height: Platform.isIOS ? 70 : 60,
      color: Colors.deepPurple,
      child: Text("START NOW", style: TextStyle(
        color: Colors.white,
        fontWeight: FontWeight.w800
      ),),
    ) ,
    );
  }
}

class SliderTile extends StatelessWidget {
  
  String imageAssetPath,title, desc;
  SliderTile({this.imageAssetPath, this.title, this.desc});
  
  @override
  Widget build(BuildContext context) {
    return Container(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Image.asset(imageAssetPath),
          SizedBox(height: 20,),
          Text(title),
          SizedBox(height: 12,),
          Text(desc)
        ],
      ),
    );
  }
}


