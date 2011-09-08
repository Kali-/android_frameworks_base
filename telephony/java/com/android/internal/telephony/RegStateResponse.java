/*
 * Copyright (C) 2007 The Android Open Source Project
 * Copyright (c) 2010, Code Aurora Forum. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.android.internal.telephony;

public class RegStateResponse {

    private String mRegStates[];

    public String[] getValues() {
        return mRegStates;
    }

    public RegStateResponse(String regstates[]) {
        this.mRegStates = regstates;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder("{");
        String[] strings = getValues();
        if (null != strings) {
            for (int i = 0; i < strings.length; i++) {
                if (null != strings[i]) {
                    sb.append(strings[i]);
                } else {
                    sb.append("null");
                }
                if (i < strings.length - 1) {
                    sb.append(",");
                }
            }
        } else {
            sb.append("null");
        }
        sb.append("}");
        return sb.toString();
    }
}


