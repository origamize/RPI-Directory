package org.rpi.rpinfo;

import java.io.Serializable;

import android.os.Parcel;
import android.os.Parcelable;

/**
 * A struct to hold information about a particular person
 */
public class QueryResultModel implements Serializable {
	//A unique identifier for this class (for serialization)
	private static final long serialVersionUID = -579697907972516780L;
	
	public String uid;
	public String name;
	public String email;
	public String year;
	public String department;
	
	public QueryResultModel(String uid, String name, String email, String year, String department){
		this.uid = uid;
		this.name = name;
		this.email = email;
		this.year = year;
		this.department = department;
	}
	
	public QueryResultModel( Parcel parcel ){
		
	}

	//Nothing interesting
	public int describeContents() {
		return 0;
	}
}
