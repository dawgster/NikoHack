//
//  HomeView.swift
//  VicinityBoxApp
//
//  Created by Nils Brand on 07.12.19.
//  Copyright © 2019 hypeTech. All rights reserved.
//

import SwiftUI

struct HomeView: View {    
    var body: some View {
        ScrollView{
               VStack {
                   MapView()
                       .frame(height:600)
                       .edgesIgnoringSafeArea(.top)
               
                HStack{
                    Spacer()
                     //Image("impacd-logo-transparent").scaleEffect(0.2)
                    Image(systemName: "cube.box.fill").scaleEffect(3.0).foregroundColor(Color.red)
                    Spacer()
                   VStack(alignment: .leading) {
                       
                       Text("Packstack 103")
                           .font(.title)
                       
                           Text("Eckstraße 2")
                               .font(.subheadline)
                    
                           Text("67661 Dansenberg-Kaiserslautern")
                               .font(.subheadline)
                       }
                       
                   .padding()
                   Spacer()
                }
            }
               }.edgesIgnoringSafeArea(.top)
               .statusBar(hidden: true)
               
    }
}

struct HomeView_Previews: PreviewProvider {
    static var previews: some View {
        HomeView()
    }
}
