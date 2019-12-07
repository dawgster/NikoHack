//
//  DeliverView.swift
//  VicinityBoxApp
//
//  Created by Nils Brand on 07.12.19.
//  Copyright © 2019 hypeTech. All rights reserved.
//

import SwiftUI

struct DeliverView: View {
    
            var body: some View {
                VStack(spacing:30) {
                            MTSlideToOpen(thumbnailLeadingTrailingPadding: 5,
                                    thumbnailColor:Color.red,
                                    thumbnailBackgroundColor: Color.red,
                                    didReachEndAction: { view in
                                               print("Slider reached end!!")
                                               DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
                                                   view.resetState()
                                               }
                                           })
                                           .frame(width: 339, height: 56)
                                           .background(Color.red)
                                           .cornerRadius(28)
                                
                     }
                }
                    /*List{
                        VStack(alignment:.leading, spacing: 10.0) {
                           TextFieldWithLabel(label:"NAME", placeholder:"Enter NAME")
                           TextFieldWithLabel(label:"TYPE", placeholder:"Enter TYPE")
                           TextFieldWithLabel(label:"ADDRESS", placeholder:"Enter ADDRESS")
                           TextFieldWithLabel(label:"PHONE", placeholder:"Enter PHONE")
                           TextFieldWithLabel(label:"DESCRIPTION", placeholder:"Enter DESCRIPTION")
                        }.listRowInsets(EdgeInsets())
                    }*/
            }


/*struct TextFieldWithLabel: View {
    var label: String
    var placeholder : String
    @State var text: String = ""
    var body: some View {
        VStack(alignment: .leading, spacing: 10.0) {
            Text(label).font(.headline)
            TextField(placeholder, text: $text)
            .padding(.all)
            .clipShape(RoundedRectangle(cornerRadius: 5.0))
            .background(Color(red: 239.0/255.0, green: 243.0/255, blue: 244.0/255.0, opacity:1.0))
        }.padding(.horizontal,15)
    }
}*/


struct DeliverView_Previews: PreviewProvider {
    static var previews: some View {
        DeliverView()
    }
}
