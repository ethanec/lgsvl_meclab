// This file was generated by a tool; you should avoid making direct changes.
// Consider using 'partial classes' to extend these types
// Input: hmi_status.proto

#pragma warning disable 0612, 1591, 3021
namespace apollo.dreamview
{

    [global::ProtoBuf.ProtoContract()]
    public partial class HMIStatus : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
        {
            return global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);
        }
        public HMIStatus()
        {
            modes = new global::System.Collections.Generic.List<string>();
            maps = new global::System.Collections.Generic.List<string>();
            vehicles = new global::System.Collections.Generic.List<string>();
            modules = new global::System.Collections.Generic.Dictionary<string, bool>();
            monitored_components = new global::System.Collections.Generic.Dictionary<string, global::apollo.monitor.ComponentStatus>();
            OnConstructor();
        }

        partial void OnConstructor();

        [global::ProtoBuf.ProtoMember(1)]
        public global::apollo.common.Header header { get; set; }

        [global::ProtoBuf.ProtoMember(2)]
        public global::System.Collections.Generic.List<string> modes { get; private set; }

        [global::ProtoBuf.ProtoMember(3)]
        [global::System.ComponentModel.DefaultValue("")]
        public string current_mode
        {
            get { return __pbn__current_mode ?? ""; }
            set { __pbn__current_mode = value; }
        }
        public bool ShouldSerializecurrent_mode()
        {
            return __pbn__current_mode != null;
        }
        public void Resetcurrent_mode()
        {
            __pbn__current_mode = null;
        }
        private string __pbn__current_mode;

        [global::ProtoBuf.ProtoMember(4)]
        public global::System.Collections.Generic.List<string> maps { get; private set; }

        [global::ProtoBuf.ProtoMember(5)]
        [global::System.ComponentModel.DefaultValue("")]
        public string current_map
        {
            get { return __pbn__current_map ?? ""; }
            set { __pbn__current_map = value; }
        }
        public bool ShouldSerializecurrent_map()
        {
            return __pbn__current_map != null;
        }
        public void Resetcurrent_map()
        {
            __pbn__current_map = null;
        }
        private string __pbn__current_map;

        [global::ProtoBuf.ProtoMember(6)]
        public global::System.Collections.Generic.List<string> vehicles { get; private set; }

        [global::ProtoBuf.ProtoMember(7)]
        [global::System.ComponentModel.DefaultValue("")]
        public string current_vehicle
        {
            get { return __pbn__current_vehicle ?? ""; }
            set { __pbn__current_vehicle = value; }
        }
        public bool ShouldSerializecurrent_vehicle()
        {
            return __pbn__current_vehicle != null;
        }
        public void Resetcurrent_vehicle()
        {
            __pbn__current_vehicle = null;
        }
        private string __pbn__current_vehicle;

        [global::ProtoBuf.ProtoMember(8)]
        [global::ProtoBuf.ProtoMap]
        public global::System.Collections.Generic.Dictionary<string, bool> modules { get; private set; }

        [global::ProtoBuf.ProtoMember(9)]
        [global::ProtoBuf.ProtoMap]
        public global::System.Collections.Generic.Dictionary<string, global::apollo.monitor.ComponentStatus> monitored_components { get; private set; }

        [global::ProtoBuf.ProtoMember(10)]
        [global::System.ComponentModel.DefaultValue("")]
        public string docker_image
        {
            get { return __pbn__docker_image ?? ""; }
            set { __pbn__docker_image = value; }
        }
        public bool ShouldSerializedocker_image()
        {
            return __pbn__docker_image != null;
        }
        public void Resetdocker_image()
        {
            __pbn__docker_image = null;
        }
        private string __pbn__docker_image;

        [global::ProtoBuf.ProtoMember(11)]
        public int utm_zone_id
        {
            get { return __pbn__utm_zone_id.GetValueOrDefault(); }
            set { __pbn__utm_zone_id = value; }
        }
        public bool ShouldSerializeutm_zone_id()
        {
            return __pbn__utm_zone_id != null;
        }
        public void Resetutm_zone_id()
        {
            __pbn__utm_zone_id = null;
        }
        private int? __pbn__utm_zone_id;

        [global::ProtoBuf.ProtoMember(12)]
        [global::System.ComponentModel.DefaultValue("")]
        public string passenger_msg
        {
            get { return __pbn__passenger_msg ?? ""; }
            set { __pbn__passenger_msg = value; }
        }
        public bool ShouldSerializepassenger_msg()
        {
            return __pbn__passenger_msg != null;
        }
        public void Resetpassenger_msg()
        {
            __pbn__passenger_msg = null;
        }
        private string __pbn__passenger_msg;

    }

}

#pragma warning restore 0612, 1591, 3021
