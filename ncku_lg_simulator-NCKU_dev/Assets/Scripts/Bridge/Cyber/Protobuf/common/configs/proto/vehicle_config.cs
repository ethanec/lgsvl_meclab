// This file was generated by a tool; you should avoid making direct changes.
// Consider using 'partial classes' to extend these types
// Input: vehicle_config.proto

#pragma warning disable 0612, 1591, 3021
namespace apollo.common
{

    [global::ProtoBuf.ProtoContract()]
    public partial class Transform : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
        {
            return global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);
        }
        public Transform()
        {
            OnConstructor();
        }

        partial void OnConstructor();

        [global::ProtoBuf.ProtoMember(1)]
        public byte[] source_frame
        {
            get { return __pbn__source_frame; }
            set { __pbn__source_frame = value; }
        }
        public bool ShouldSerializesource_frame()
        {
            return __pbn__source_frame != null;
        }
        public void Resetsource_frame()
        {
            __pbn__source_frame = null;
        }
        private byte[] __pbn__source_frame;

        [global::ProtoBuf.ProtoMember(2)]
        public byte[] target_frame
        {
            get { return __pbn__target_frame; }
            set { __pbn__target_frame = value; }
        }
        public bool ShouldSerializetarget_frame()
        {
            return __pbn__target_frame != null;
        }
        public void Resettarget_frame()
        {
            __pbn__target_frame = null;
        }
        private byte[] __pbn__target_frame;

        [global::ProtoBuf.ProtoMember(3)]
        public Point3D translation { get; set; }

        [global::ProtoBuf.ProtoMember(4)]
        public Quaternion rotation { get; set; }

    }

    [global::ProtoBuf.ProtoContract()]
    public partial class Extrinsics : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
        {
            return global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);
        }
        public Extrinsics()
        {
            tansforms = new global::System.Collections.Generic.List<Transform>();
            OnConstructor();
        }

        partial void OnConstructor();

        [global::ProtoBuf.ProtoMember(1)]
        public global::System.Collections.Generic.List<Transform> tansforms { get; private set; }

    }

    [global::ProtoBuf.ProtoContract()]
    public partial class VehicleID : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
        {
            return global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);
        }
        public VehicleID()
        {
            OnConstructor();
        }

        partial void OnConstructor();

        [global::ProtoBuf.ProtoMember(1)]
        [global::System.ComponentModel.DefaultValue("")]
        public string vin
        {
            get { return __pbn__vin ?? ""; }
            set { __pbn__vin = value; }
        }
        public bool ShouldSerializevin()
        {
            return __pbn__vin != null;
        }
        public void Resetvin()
        {
            __pbn__vin = null;
        }
        private string __pbn__vin;

        [global::ProtoBuf.ProtoMember(2)]
        [global::System.ComponentModel.DefaultValue("")]
        public string plate
        {
            get { return __pbn__plate ?? ""; }
            set { __pbn__plate = value; }
        }
        public bool ShouldSerializeplate()
        {
            return __pbn__plate != null;
        }
        public void Resetplate()
        {
            __pbn__plate = null;
        }
        private string __pbn__plate;

        [global::ProtoBuf.ProtoMember(3)]
        [global::System.ComponentModel.DefaultValue("")]
        public string other_unique_id
        {
            get { return __pbn__other_unique_id ?? ""; }
            set { __pbn__other_unique_id = value; }
        }
        public bool ShouldSerializeother_unique_id()
        {
            return __pbn__other_unique_id != null;
        }
        public void Resetother_unique_id()
        {
            __pbn__other_unique_id = null;
        }
        private string __pbn__other_unique_id;

    }

    [global::ProtoBuf.ProtoContract()]
    public partial class VehicleParam : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
        {
            return global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);
        }
        public VehicleParam()
        {
            OnConstructor();
        }

        partial void OnConstructor();

        [global::ProtoBuf.ProtoMember(1)]
        [global::System.ComponentModel.DefaultValue(VehicleBrand.LincolnMkz)]
        public VehicleBrand brand
        {
            get { return __pbn__brand ?? VehicleBrand.LincolnMkz; }
            set { __pbn__brand = value; }
        }
        public bool ShouldSerializebrand()
        {
            return __pbn__brand != null;
        }
        public void Resetbrand()
        {
            __pbn__brand = null;
        }
        private VehicleBrand? __pbn__brand;

        [global::ProtoBuf.ProtoMember(2)]
        public VehicleID vehicle_id { get; set; }

        [global::ProtoBuf.ProtoMember(3)]
        [global::System.ComponentModel.DefaultValue(double.NaN)]
        public double front_edge_to_center
        {
            get { return __pbn__front_edge_to_center ?? double.NaN; }
            set { __pbn__front_edge_to_center = value; }
        }
        public bool ShouldSerializefront_edge_to_center()
        {
            return __pbn__front_edge_to_center != null;
        }
        public void Resetfront_edge_to_center()
        {
            __pbn__front_edge_to_center = null;
        }
        private double? __pbn__front_edge_to_center;

        [global::ProtoBuf.ProtoMember(4)]
        [global::System.ComponentModel.DefaultValue(double.NaN)]
        public double back_edge_to_center
        {
            get { return __pbn__back_edge_to_center ?? double.NaN; }
            set { __pbn__back_edge_to_center = value; }
        }
        public bool ShouldSerializeback_edge_to_center()
        {
            return __pbn__back_edge_to_center != null;
        }
        public void Resetback_edge_to_center()
        {
            __pbn__back_edge_to_center = null;
        }
        private double? __pbn__back_edge_to_center;

        [global::ProtoBuf.ProtoMember(5)]
        [global::System.ComponentModel.DefaultValue(double.NaN)]
        public double left_edge_to_center
        {
            get { return __pbn__left_edge_to_center ?? double.NaN; }
            set { __pbn__left_edge_to_center = value; }
        }
        public bool ShouldSerializeleft_edge_to_center()
        {
            return __pbn__left_edge_to_center != null;
        }
        public void Resetleft_edge_to_center()
        {
            __pbn__left_edge_to_center = null;
        }
        private double? __pbn__left_edge_to_center;

        [global::ProtoBuf.ProtoMember(6)]
        [global::System.ComponentModel.DefaultValue(double.NaN)]
        public double right_edge_to_center
        {
            get { return __pbn__right_edge_to_center ?? double.NaN; }
            set { __pbn__right_edge_to_center = value; }
        }
        public bool ShouldSerializeright_edge_to_center()
        {
            return __pbn__right_edge_to_center != null;
        }
        public void Resetright_edge_to_center()
        {
            __pbn__right_edge_to_center = null;
        }
        private double? __pbn__right_edge_to_center;

        [global::ProtoBuf.ProtoMember(7)]
        [global::System.ComponentModel.DefaultValue(double.NaN)]
        public double length
        {
            get { return __pbn__length ?? double.NaN; }
            set { __pbn__length = value; }
        }
        public bool ShouldSerializelength()
        {
            return __pbn__length != null;
        }
        public void Resetlength()
        {
            __pbn__length = null;
        }
        private double? __pbn__length;

        [global::ProtoBuf.ProtoMember(8)]
        [global::System.ComponentModel.DefaultValue(double.NaN)]
        public double width
        {
            get { return __pbn__width ?? double.NaN; }
            set { __pbn__width = value; }
        }
        public bool ShouldSerializewidth()
        {
            return __pbn__width != null;
        }
        public void Resetwidth()
        {
            __pbn__width = null;
        }
        private double? __pbn__width;

        [global::ProtoBuf.ProtoMember(9)]
        [global::System.ComponentModel.DefaultValue(double.NaN)]
        public double height
        {
            get { return __pbn__height ?? double.NaN; }
            set { __pbn__height = value; }
        }
        public bool ShouldSerializeheight()
        {
            return __pbn__height != null;
        }
        public void Resetheight()
        {
            __pbn__height = null;
        }
        private double? __pbn__height;

        [global::ProtoBuf.ProtoMember(10)]
        [global::System.ComponentModel.DefaultValue(double.NaN)]
        public double min_turn_radius
        {
            get { return __pbn__min_turn_radius ?? double.NaN; }
            set { __pbn__min_turn_radius = value; }
        }
        public bool ShouldSerializemin_turn_radius()
        {
            return __pbn__min_turn_radius != null;
        }
        public void Resetmin_turn_radius()
        {
            __pbn__min_turn_radius = null;
        }
        private double? __pbn__min_turn_radius;

        [global::ProtoBuf.ProtoMember(11)]
        [global::System.ComponentModel.DefaultValue(double.NaN)]
        public double max_acceleration
        {
            get { return __pbn__max_acceleration ?? double.NaN; }
            set { __pbn__max_acceleration = value; }
        }
        public bool ShouldSerializemax_acceleration()
        {
            return __pbn__max_acceleration != null;
        }
        public void Resetmax_acceleration()
        {
            __pbn__max_acceleration = null;
        }
        private double? __pbn__max_acceleration;

        [global::ProtoBuf.ProtoMember(12)]
        [global::System.ComponentModel.DefaultValue(double.NaN)]
        public double max_deceleration
        {
            get { return __pbn__max_deceleration ?? double.NaN; }
            set { __pbn__max_deceleration = value; }
        }
        public bool ShouldSerializemax_deceleration()
        {
            return __pbn__max_deceleration != null;
        }
        public void Resetmax_deceleration()
        {
            __pbn__max_deceleration = null;
        }
        private double? __pbn__max_deceleration;

        [global::ProtoBuf.ProtoMember(13)]
        [global::System.ComponentModel.DefaultValue(double.NaN)]
        public double max_steer_angle
        {
            get { return __pbn__max_steer_angle ?? double.NaN; }
            set { __pbn__max_steer_angle = value; }
        }
        public bool ShouldSerializemax_steer_angle()
        {
            return __pbn__max_steer_angle != null;
        }
        public void Resetmax_steer_angle()
        {
            __pbn__max_steer_angle = null;
        }
        private double? __pbn__max_steer_angle;

        [global::ProtoBuf.ProtoMember(14)]
        [global::System.ComponentModel.DefaultValue(double.NaN)]
        public double max_steer_angle_rate
        {
            get { return __pbn__max_steer_angle_rate ?? double.NaN; }
            set { __pbn__max_steer_angle_rate = value; }
        }
        public bool ShouldSerializemax_steer_angle_rate()
        {
            return __pbn__max_steer_angle_rate != null;
        }
        public void Resetmax_steer_angle_rate()
        {
            __pbn__max_steer_angle_rate = null;
        }
        private double? __pbn__max_steer_angle_rate;

        [global::ProtoBuf.ProtoMember(15)]
        [global::System.ComponentModel.DefaultValue(double.NaN)]
        public double min_steer_angle_rate
        {
            get { return __pbn__min_steer_angle_rate ?? double.NaN; }
            set { __pbn__min_steer_angle_rate = value; }
        }
        public bool ShouldSerializemin_steer_angle_rate()
        {
            return __pbn__min_steer_angle_rate != null;
        }
        public void Resetmin_steer_angle_rate()
        {
            __pbn__min_steer_angle_rate = null;
        }
        private double? __pbn__min_steer_angle_rate;

        [global::ProtoBuf.ProtoMember(16)]
        [global::System.ComponentModel.DefaultValue(double.NaN)]
        public double steer_ratio
        {
            get { return __pbn__steer_ratio ?? double.NaN; }
            set { __pbn__steer_ratio = value; }
        }
        public bool ShouldSerializesteer_ratio()
        {
            return __pbn__steer_ratio != null;
        }
        public void Resetsteer_ratio()
        {
            __pbn__steer_ratio = null;
        }
        private double? __pbn__steer_ratio;

        [global::ProtoBuf.ProtoMember(17)]
        [global::System.ComponentModel.DefaultValue(double.NaN)]
        public double wheel_base
        {
            get { return __pbn__wheel_base ?? double.NaN; }
            set { __pbn__wheel_base = value; }
        }
        public bool ShouldSerializewheel_base()
        {
            return __pbn__wheel_base != null;
        }
        public void Resetwheel_base()
        {
            __pbn__wheel_base = null;
        }
        private double? __pbn__wheel_base;

        [global::ProtoBuf.ProtoMember(18)]
        [global::System.ComponentModel.DefaultValue(double.NaN)]
        public double wheel_rolling_radius
        {
            get { return __pbn__wheel_rolling_radius ?? double.NaN; }
            set { __pbn__wheel_rolling_radius = value; }
        }
        public bool ShouldSerializewheel_rolling_radius()
        {
            return __pbn__wheel_rolling_radius != null;
        }
        public void Resetwheel_rolling_radius()
        {
            __pbn__wheel_rolling_radius = null;
        }
        private double? __pbn__wheel_rolling_radius;

        [global::ProtoBuf.ProtoMember(19)]
        [global::System.ComponentModel.DefaultValue(float.NaN)]
        public float max_abs_speed_when_stopped
        {
            get { return __pbn__max_abs_speed_when_stopped ?? float.NaN; }
            set { __pbn__max_abs_speed_when_stopped = value; }
        }
        public bool ShouldSerializemax_abs_speed_when_stopped()
        {
            return __pbn__max_abs_speed_when_stopped != null;
        }
        public void Resetmax_abs_speed_when_stopped()
        {
            __pbn__max_abs_speed_when_stopped = null;
        }
        private float? __pbn__max_abs_speed_when_stopped;

        [global::ProtoBuf.ProtoMember(20)]
        [global::System.ComponentModel.DefaultValue(double.NaN)]
        public double brake_deadzone
        {
            get { return __pbn__brake_deadzone ?? double.NaN; }
            set { __pbn__brake_deadzone = value; }
        }
        public bool ShouldSerializebrake_deadzone()
        {
            return __pbn__brake_deadzone != null;
        }
        public void Resetbrake_deadzone()
        {
            __pbn__brake_deadzone = null;
        }
        private double? __pbn__brake_deadzone;

        [global::ProtoBuf.ProtoMember(21)]
        [global::System.ComponentModel.DefaultValue(double.NaN)]
        public double throttle_deadzone
        {
            get { return __pbn__throttle_deadzone ?? double.NaN; }
            set { __pbn__throttle_deadzone = value; }
        }
        public bool ShouldSerializethrottle_deadzone()
        {
            return __pbn__throttle_deadzone != null;
        }
        public void Resetthrottle_deadzone()
        {
            __pbn__throttle_deadzone = null;
        }
        private double? __pbn__throttle_deadzone;

    }

    [global::ProtoBuf.ProtoContract()]
    public partial class VehicleConfig : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
        {
            return global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);
        }
        public VehicleConfig()
        {
            OnConstructor();
        }

        partial void OnConstructor();

        [global::ProtoBuf.ProtoMember(1)]
        public Header header { get; set; }

        [global::ProtoBuf.ProtoMember(2)]
        public VehicleParam vehicle_param { get; set; }

        [global::ProtoBuf.ProtoMember(3)]
        public Extrinsics extrinsics { get; set; }

    }

    [global::ProtoBuf.ProtoContract()]
    public enum VehicleBrand
    {
        [global::ProtoBuf.ProtoEnum(Name = @"LINCOLN_MKZ")]
        LincolnMkz = 0,
        [global::ProtoBuf.ProtoEnum(Name = @"GEM")]
        Gem = 1,
        [global::ProtoBuf.ProtoEnum(Name = @"LEXUS")]
        Lexus = 2,
        [global::ProtoBuf.ProtoEnum(Name = @"TRANSIT")]
        Transit = 3,
        [global::ProtoBuf.ProtoEnum(Name = @"GE3")]
        Ge3 = 4,
        [global::ProtoBuf.ProtoEnum(Name = @"WEY")]
        Wey = 5,
        [global::ProtoBuf.ProtoEnum(Name = @"ZHONGYUN")]
        Zhongyun = 6,
        [global::ProtoBuf.ProtoEnum(Name = @"CH")]
        Ch = 7,
    }

}

#pragma warning restore 0612, 1591, 3021
