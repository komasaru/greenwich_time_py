module Greenwich
  #===========================================================================
  # Module for angles
  #===========================================================================
  module Angle
    module_function

    #-------------------------------------------------------------------------
    # Normalize angle into the range 0 <= a < 2pi.
    #
    # @param:  angle  (Before normalized)
    # @return: angle  (Normalized angle)
    #-------------------------------------------------------------------------
    def norm_angle(angle)
      while angle <   0; angle += PI2; end
      while angle > PI2; angle -= PI2; end
      return angle
    rescue => e
      raise
    end
  end
end

