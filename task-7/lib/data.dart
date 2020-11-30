import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class SliderModel{

  String imagePath;
  String title;
  String desc;

  SliderModel({this.imagePath, this.title,this.desc});

  void setImageAssetPath(String getImagepath){
    imagePath = getImagepath;
  }

  void setTitle(String getTitle){
    title = getTitle;
  }

  void setDesc(String getDesc){
    desc = getDesc;
  }

 String getImageAssetPath(){
    return imagePath;
 }

 String getTitle(){
    return title;
 }

 String getDesc(){
    return desc;
 }
}

List<SliderModel> getSlides(){

  List<SliderModel> slides = new List<SliderModel>();
  SliderModel sliderModel = new SliderModel();

  //1
  sliderModel.setImageAssetPath("assets/IMG_3999.jpg");
  sliderModel.setTitle("HELLO!");
  sliderModel.setDesc("You found the right destination for your next great read");
  slides.add(sliderModel);

  sliderModel = new SliderModel();

 //2
  sliderModel.setImageAssetPath("assets/IMG_4003.PNG");
  sliderModel.setTitle("AWESOME");
  sliderModel.setDesc("Get access to all our books at anytime anywhere");
  slides.add(sliderModel);

  sliderModel = new SliderModel();

  return slides;

}