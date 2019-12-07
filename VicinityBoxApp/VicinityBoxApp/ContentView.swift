//
//  ContentView.swift
//  VicinityBoxApp
//
//  Created by Nils Brand on 07.12.19.
//  Copyright © 2019 hypeTech. All rights reserved.
//

import SwiftUI

struct ContentView: View {
    
   // init() { //for Tabbar backgroundColor ...
   //     UITabBar.appearance().backgroundColor = UIColor.blue
    //}
    
    
    @State  var tabSelected = 0
    
    var body: some View {
        
        TabView(selection: $tabSelected) {
           
            HomeView()
                .tabItem {
                    Image(systemName: "house")
                    Text("Welcome")
            }.tag(1)
                
            
            
            PickUpView()
                .tabItem {
                    Image(systemName: "tray.and.arrow.down.fill")
                    Text("Pick Up")
            }.tag(2)
            
            
            DeliverView()
                .tabItem {
                    Image(systemName: "tray.and.arrow.up")
                    Text("Deliver")
            }.tag(3)
            
            
        InfoView()
                .tabItem {
                    Image(systemName: "info.circle.fill")
                    Text("Info")
            }.tag(4)
        }
        .font(.headline).accentColor(Color.red)
         .statusBar(hidden: true).edgesIgnoringSafeArea(.top)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
